"use client";

import { useState } from "react";

export default function SetupPage() {
  const [form, setForm] = useState({
    ELEVENLABS_API_KEY: "",
    ELEVENLABS_VOICE_ID: "",
    ELEVENLABS_AGENT_ID: "",
    GROQ_API_KEY: "",
    OPENAI_API_KEY: "",
    ANTHROPIC_API_KEY: "",
    PRIMARY_LLM_PROVIDER: "groq",
    LLM_FALLBACK: "",
    NEXT_PUBLIC_PROJECT_NAME: "JessVoiceAgent",
    NEXT_PUBLIC_BACKEND_URL: "http://localhost:8000",
  });
  const [status, setStatus] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    const res = await fetch(${process.env.NEXT_PUBLIC_BACKEND_URL}/api/save-config", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form),
    });
    if (res.ok) {
      setStatus("saved");
      window.location.href = "/";
    } else {
      setStatus("error");
    }
  };

  return (
    <main style={{ maxWidth: 600, margin: "2rem auto" }}>
      <h1 className="text-xl font-bold mb-4">Initial Configuration</h1>
      <form onSubmit={handleSubmit} className="flex flex-col gap-2">
        {Object.entries(form).map(([key, val]) => (
          <input
            key={key}
            name={key}
            value={val}
            placeholder={key}
            onChange={handleChange}
            className="border p-2"
            required={key.startsWith("ELEVENLABS") || key === "NEXT_PUBLIC_PROJECT_NAME" || key === "NEXT_PUBLIC_BACKEND_URL"}
          />
        ))}
        <button className="border p-2" type="submit">
          Save
        </button>
        {status === "error" && <p className="text-red-500">Failed to save configuration.</p>}
      </form>
    </main>
  );
}
