# Number Guessing Game (Java Console)

**Track:** Java Development — Task 2
**Program:** Oasis Infobyte SIP

## Objective
The computer picks a random number; the player guesses it with higher/lower hints, a limited number of attempts, difficulty levels, and a running score summary.

## Tech Stack
Java (console application) — `java.util.Random`, `Scanner`, standard library only.

## Features
- Random number generated at the start of every round
- "Too High!" / "Too Low!" / "Correct!" feedback after each guess
- Visible attempt counter (e.g. "Attempt 3/7")
- Maximum attempts enforced — "You Lost!" with the number revealed if exceeded
- "Play again?" prompt after each round
- Running score summary across all rounds played in the session
- **Bonus implemented:** 3 difficulty levels — Easy (1–50, 10 attempts), Medium (1–100, 7 attempts), Hard (1–200, 5 attempts)
- Non-numeric guesses are rejected without costing an attempt

## How to Compile & Run
```
javac NumberGuessingGame.java
java NumberGuessingGame
```

## Testing Performed
- **Win path:** played Medium (1–100) using an automated binary-search strategy — correctly guessed in 6 of 7 allowed attempts, round summary printed correctly. ✅
- **Loss path:** played Hard (1–200) with 5 non-winning guesses — game correctly ended with "You Lost!", revealed the number, and logged it as a loss in the final summary. ✅
- **Invalid input:** a non-numeric guess ("abc") was rejected with an error message and did **not** consume an attempt. ✅

## Author
_Add your name here before submitting._
