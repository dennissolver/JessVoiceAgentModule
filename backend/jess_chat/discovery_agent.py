# backend/jess_chat/discovery_agent.py

def handle_discovery_prompt(prompt: str) -> str:
    prompt_lower = prompt.lower()

    # SPIN: Situation
    if any(q in prompt_lower for q in ["just getting started", "new project", "starting out", "current setup"]):
        return "Can you describe your current situation or setup for me?"

    # SPIN: Problem
    elif any(q in prompt_lower for q in ["problem", "challenge", "issue", "pain", "frustrated", "struggle"]):
        return "Can you tell me more about the challenges you're facing?"

    # SPIN: Implication
    elif any(q in prompt_lower for q in ["consequence", "impact", "effect", "risk", "result if unresolved"]):
        return "What happens if this challenge continues without a solution?"

    # SPIN: Need-payoff
    elif any(q in prompt_lower for q in ["ideal", "benefit", "value", "outcome", "result if solved"]):
        return "What would a successful outcome look like for you?"

    # MERRIT: Motivations
    elif any(q in prompt_lower for q in ["goal", "vision", "motivation", "why", "what are you aiming for"]):
        return "What’s motivating this project — what's your big picture goal?"

    # MERRIT: Expectations
    elif any(q in prompt_lower for q in ["expect", "result", "success", "ideal result"]):
        return "What expectations or results are most important to you?"

    # MERRIT: Risks
    elif any(q in prompt_lower for q in ["worried", "risk", "concern", "hesitation"]):
        return "Are there any risks or concerns you’re trying to avoid?"

    # MERRIT: Resources
    elif any(q in prompt_lower for q in ["budget", "team", "tools", "timeframe", "deadline", "resources"]):
        return "What resources do you have or plan to use — time, team, budget?"

    # MERRIT: Impact
    elif any(q in prompt_lower for q in ["impact", "who it helps", "stakeholders", "business value"]):
        return "Who or what will be impacted most if this is successful?"

    # MERRIT: Timeline
    elif any(q in prompt_lower for q in ["when", "timeline", "launch", "urgency", "milestone"]):
        return "What’s your ideal timeline or milestone for progress?"

    # Fallback default
    return "Tell me more about your project or what you’re trying to achieve."

