// Embeddable Jess Widget
class JessAgent extends HTMLElement {
  constructor() {
    super();
    const shadow = this.attachShadow({ mode: "open" });
    const btn = document.createElement("button");
    btn.textContent = "🎤 Talk to Jess";
    btn.onclick = () => window.open("http://localhost:3000", "_blank");
    shadow.appendChild(btn);
  }
}
customElements.define("jess-agent", JessAgent);
