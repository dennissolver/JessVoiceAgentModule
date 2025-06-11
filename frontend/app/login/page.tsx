"use client";
import { useState } from "react";

export default function LoginPage() {
  const [email, setEmail] = useState("admin@example.com");
  const [password, setPassword] = useState("admin");
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/auth/jwt/login`, {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: new URLSearchParams({ username: email, password }),
    });
    if (res.ok) {
      const data = await res.json();
      localStorage.setItem("token", data.access_token);
      window.location.href = "/";
    } else {
      setError("Invalid credentials");
    }
  };

  return (
    <main style={{ maxWidth: 400, margin: "2rem auto" }}>
      <h1 className="text-xl font-bold mb-4">Login</h1>
      <form onSubmit={handleSubmit} className="flex flex-col gap-2">
        <input
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
          className="border p-2"
        />
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password"
          className="border p-2"
        />
        <button className="border p-2" type="submit">
          Login
        </button>
        {error && <p className="text-red-500">{error}</p>}
      </form>
    </main>
  );
}
