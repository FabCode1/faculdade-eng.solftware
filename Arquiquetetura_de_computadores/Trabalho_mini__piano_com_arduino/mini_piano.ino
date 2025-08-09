// --- Definição dos pinos para as notas e botões ---
int nota1 = 2;
int nota2 = 3;
int nota3 = 4;
int nota4 = 5;
int nota5 = 6;
int nota6 = 7;
int nota7 = 8;
int nota8 = 9;

int botaoMusica = 11; // Botão que toca a música
int buzzer = 10;      // Pino do buzzer
int ledNota = 1;
bool botaoPressionado = false; // Para evitar repetição contínua

// --- Frequências das notas usadas ---
#define D4  293
#define E4  329
#define F4  349
#define G4  392
#define A4  440
#define Bb4 466
#define B4  494
#define C5  523
#define D5  587
#define Eb5 622
#define F5  698
#define G5  784
#define C4  261

void setup() {
  pinMode(nota1, INPUT);
  pinMode(nota2, INPUT);
  pinMode(nota3, INPUT);
  pinMode(nota4, INPUT);
  pinMode(nota5, INPUT);
  pinMode(nota6, INPUT);
  pinMode(nota7, INPUT);
  pinMode(nota8, INPUT);
  pinMode(botaoMusica, INPUT);

  pinMode(buzzer, OUTPUT);
  pinMode(ledNota, OUTPUT);
}

void loop() {
  bool estadoAtual = digitalRead(botaoMusica);
  if (estadoAtual == HIGH && !botaoPressionado) {
    midi(); // Toca a melodia MIDI personalizada
    botaoPressionado = true;
  }
  if (estadoAtual == LOW) {
    botaoPressionado = false;
  }

  if (digitalRead(nota1) == HIGH) {
    tone(buzzer, C4, 100);
    digitalWrite(ledNota, HIGH);
  } else if (digitalRead(nota2) == HIGH) {
    tone(buzzer, D4, 100);
    digitalWrite(ledNota, HIGH);
  } else if (digitalRead(nota3) == HIGH) {
    tone(buzzer, E4, 100);
    digitalWrite(ledNota, HIGH);
  } else if (digitalRead(nota4) == HIGH) {
    tone(buzzer, F4, 100);
    digitalWrite(ledNota, HIGH);
  } else if (digitalRead(nota5) == HIGH) {
    tone(buzzer, G4, 100);
    digitalWrite(ledNota, HIGH);
  } else if (digitalRead(nota6) == HIGH) {
    tone(buzzer, A4, 100);
    digitalWrite(ledNota, HIGH);
  } else if (digitalRead(nota7) == HIGH) {
    tone(buzzer, B4, 100);
  } else if (digitalRead(nota8) == HIGH) {
    tone(buzzer, C5, 100);
    digitalWrite(ledNota, HIGH);
  } else {
    noTone(buzzer);
    digitalWrite(ledNota, LOW);
  }

  delay(10); // Anti-rebote básico
}

void midi() {
  int tonePin = buzzer;
  tone(tonePin, A4, 336); delay(374); noTone(tonePin); delay(10);
  tone(tonePin, Bb4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, D4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, G4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, Bb4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, C5, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, F4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, A4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, Bb4, 336); delay(374); noTone(tonePin); delay(20);
  tone(tonePin, G4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, Bb4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, D5, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, Eb5, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, G4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, D5, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, C5, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, Bb4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, D4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, G4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, Bb4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, C5, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, F4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, A4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, Bb4, 336); delay(374); noTone(tonePin); delay(20);
  tone(tonePin, G4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, Bb4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, D5, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, Eb5, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, G4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, D5, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, C5, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, Bb4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, D4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, G4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, Bb4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, A4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, C4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, F4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, G4, 336); delay(374); noTone(tonePin); delay(20);
  tone(tonePin, C4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, F4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, G4, 336); delay(374); noTone(tonePin); delay(20);
  tone(tonePin, F4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, G4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, A4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, Bb4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, D4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, G4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, Bb4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, C5, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, F4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, A4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, Bb4, 336); delay(374); noTone(tonePin); delay(20);
  tone(tonePin, G4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, Bb4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, D5, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, Eb5, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, G4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, D5, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, C5, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, Bb4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, D4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, G4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, Bb4, 168); delay(187); noTone(tonePin); delay(10);
  tone(tonePin, A4, 168); delay(187); noTone(tonePin); delay(10);
}
