export default function Layout({ children }: { children: React.ReactNode }) {
  const agentUrl = process.env.NEXT_PUBLIC_JESS_AGENT_URL;
  return (
    <html lang="en">
      <head>
        {agentUrl && (
          <script
            dangerouslySetInnerHTML={{
              __html: `window.JESS_AGENT_URL = "${agentUrl}";`,
            }}
          />
        )}
      </head>
      <body style={{ fontFamily: 'Arial, sans-serif', padding: '1rem' }}>
        {children}
      </body>
    </html>
  );
}
