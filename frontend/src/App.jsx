import './App.css';
import { SyncOutlined } from '@ant-design/icons';
import { Bubble, Sender } from '@ant-design/x';
import XMarkdown from '@ant-design/x-markdown';
import { OpenAIChatProvider, useXChat, XRequest } from '@ant-design/x-sdk';
import { Button, Flex, Tooltip } from 'antd';
import React from 'react';

const role = {
  assistant: {
    placement: 'end',
    contentRender(content) {
      debugger;
      const newContent = content.replace(/\n\n/g, '<br/><br/>');
      return <XMarkdown content={newContent} />;
    },
    className: "ai",
    style: {
      backGround: "#7d6ef2"
    }
  },
  user: {
    placement: 'start',
  },
};


const App = () => {
  const [content, setContent] = React.useState('');
  const [provider] = React.useState(
    new OpenAIChatProvider({
      request: XRequest('http://localhost:5000', {
        manual: true,
        fetch: async (url, options) => {
          const result = await fetch(`${url}/agent`, {
            ...options,
          });
          let history = JSON.parse(options.body);
          history = history.messages || [];
          const copy = result.clone()
          const response = await copy.json();
          debugger
          setMessages([...history.map((i, index) => {
            return {
              id: Date.now() + index,
              message: { ...i },
              status: 'success',
            }
          }), {
            id: Date.now(),
            message: { role: 'assistant', content: response?.message || 'Error in message'},
            status: 'success',
          },
        ])
        return result;
        },        
      }),
    }),
  );

    const {
    onRequest,
    messages,
    setMessages,
    setMessage,
    isRequesting,
    abort,
    onReload,
  } = useXChat({
    provider,
    defaultMessages: [],
    requestFallback: (config, { error, errorInfo, messageInfo }) => {
      debugger
      if (error.name === 'AbortError') {
        return {
          content: "Error 1",
          role: 'assistant',
        };
      }
      debugger
      return config?.messages[0] || {
          content: "Error 2",
          role: 'assistant',
      };
    },
    requestPlaceholder: () => {
      return {
        content: 'loading',
        role: 'assistant',
      };
    },
  });
  
  console.log(messages);
  return (
    <Flex vertical gap="middle">      
      {/* Message list: display all chat messages, including historical messages */}
      <Bubble.List
        style={{ height: 500 }}
        role={role}
        items={messages.filter(({ id, message, status}) =>  message.content !== '').map(({ id, message, status }) => {
          return ({
          key: Math.random(),
          role: message.role,
          status: status,
          loading: status === 'loading',
          content: message.content,
          components:
            message.role === 'assistant'
              ? {
                  footer: (
                    <Tooltip title={"entry"}>
                      <Button
                        size="small"
                        type="text"
                        icon={<SyncOutlined />}
                        style={{ marginInlineEnd: 'auto' }}
                        onClick={() =>
                          onReload(id, {
                            userAction: 'retry',
                          })
                        }
                      />
                    </Tooltip>
                  ),
                }
              : {},
        })
        }
        )}
      />
      <Sender
        loading={isRequesting}
        value={content}
        onCancel={() => {
          abort();
        }}
        onChange={setContent}
        placeholder={"Ask your questions"}
        onSubmit={nextContent => {
          debugger;
          onRequest({
            messages: [
              {
                role: 'user',
                content: nextContent,
              },
            ],
            thinking: {
              type: 'disabled',
            },
          });
          setContent('');
        }}
      />
    </Flex>
  );
};

export default App;
