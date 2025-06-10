// Embeddable Jess Widget
class JessAgent extends HTMLElement {
  constructor() {
    super();
    const shadow = this.attachShadow({ mode: "open" });
    const btn = document.createElement("button");
    btn.textContent = "🎤 Talk to Jess";
    const targetURL = window?.JESS_AGENT_URL || "http://localhost:3000";
    btn.onclick = () => window.open(targetURL, "_blank");

    shadow.appendChild(btn);
  }
}
customElements.define("jess-agent", JessAgent);
