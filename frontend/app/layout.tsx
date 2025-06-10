export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head />
      <script
        dangerouslySetInnerHTML={{
          __html: `window.JESS_AGENT_URL = "${process.env.NEXT_PUBLIC_JESS_AGENT_URL}";`,
        }}
      ></script>

      <body style={{ fontFamily: 'Arial, sans-serif', padding: '1rem' }}>
        {children}
      </body>
    </html>
  );
}
