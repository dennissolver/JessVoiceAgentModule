export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head />
      <body style={{ fontFamily: 'Arial, sans-serif', padding: '1rem' }}>
        {children}
      </body>
    </html>
  );
}
