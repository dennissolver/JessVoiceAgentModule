"use client";

import { useEffect, useRef } from "react";

export default function Home() {
  const isRecognizing = useRef(false);

  useEffect(() => {
    async function initVoiceAgent() {
      try {
        await navigator.mediaDevices.getUserMedia({ audio: true });
        console.log("✅ Microphone access granted");

        const SpeechRecognition =
          window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = new SpeechRecognition();

        recognition.continuous = true;
        recognition.lang = "en-US";
        recognition.interimResults = false;

        recognition.onresult = async (event) => {
          try {
            const results = Array.from(event.results);
            const transcript = results
              .map((r) => r[0].transcript)
              .join(" ")
              .trim();

            if (!transcript) return;
            console.log("🗣️ Final transcript:", transcript);
            console.log("📡 Sending to backend:", transcript);

            const BACKEND_URL = process.env.NEXT_PUBLIC_BACKEND_URL || "";
            const response = await fetch(`${BACKEND_URL}/chat`, {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({
                prompt: transcript,
                session_id: "default",
              }),
            });

            if (!response.ok) {
              const errorText = await response.text();
              console.error(`❌ Backend error ${response.status}:`, errorText);
              return;
            }

            const data = await response.json();
            console.log("🤖 Jess replied:", data.reply);
            console.log("🔊 Audio base64 preview:", data.audio?.slice(0, 50));

            if (data.audio) {
              const audio = new Audio("data:audio/mp3;base64," + data.audio);
              audio.play().catch((e) =>
                console.error("🔈 Audio playback failed:", e)
              );
            } else {
              console.warn("⚠️ No audio returned from backend.");
            }
          } catch (err) {
            console.error("❌ Error processing recognition result:", err);
          }
        };

        recognition.onerror = (event) => {
          console.error("🎤 Speech error:", event);
          isRecognizing.current = false;

          if (
            event.error === "no-speech" ||
            event.error === "aborted" ||
            event.error === "audio-capture"
          ) {
            console.log("🔁 Attempting to restart after error...");
            try {
              recognition.start();
              isRecognizing.current = true;
            } catch (e) {
              console.warn("⚠️ Restart after error failed:", e);
            }
          }
        };

        recognition.onend = () => {
          console.log("🔁 Recognition ended.");
          if (!isRecognizing.current) {
            try {
              recognition.start();
              isRecognizing.current = true;
            } catch (e) {
              console.warn("⚠️ Recognition restart error:", e);
            }
          }
        };

        recognition.start();
        isRecognizing.current = true;
      } catch (err) {
        console.error("🚫 Microphone access denied or recognition setup failed:", err);
      }
    }

    initVoiceAgent();
  }, []);

  return (
    <main className="p-6">
      <h1 className="text-xl font-bold mb-4">🎙️ Jess Voice Agent</h1>
      <p>Start talking and Jess will reply...</p>
    </main>
  );
}
