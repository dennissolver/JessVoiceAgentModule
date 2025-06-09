export {};

declare global {
  interface SpeechRecognitionEvent extends Event {
    results: SpeechRecognitionResultList;
  }

  interface SpeechRecognitionResultList extends Array<SpeechRecognitionResult> {}

  interface SpeechRecognitionResult {
    isFinal: boolean;
    0: SpeechRecognitionAlternative;
  }

  interface SpeechRecognitionAlternative {
    transcript: string;
    confidence: number;
  }

  interface Window {
    SpeechRecognition: any;
    webkitSpeechRecognition: any;
  }
    // Add this to frontend/types/speech.d.ts
  interface SpeechRecognitionErrorEvent extends Event {
    error: string;
  }
  
}
