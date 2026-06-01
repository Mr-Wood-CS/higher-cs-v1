# Slide 1: Space Invaders Lesson 7 - Game Over Conditions

- Learning Intention: Define and code win/lose conditions.
- E&Os: `TCH 3-15a`, `TCH 3-13a`, `TCH 3-14b`
- Benchmarks focus: system interaction between sprites, lives, and game state.

# Slide 2: Success Criteria

- I can reduce life when threats reach player/bottom.
- I can detect zero lives and end game.
- I can explain why clear end conditions matter.

# Slide 3: Starter / Retrieval

- What should cause life loss in our game?
- Is overlap with player enough, or should bottom-screen checks also count?

# Slide 4: Teacher Demo - Player Collision Route

- Use overlap event: `Enemy` overlaps `Player`.
- Apply `info.changeLifeBy(-1)`.
- Destroy enemy on impact.

# Slide 5: Teacher Demo - Bottom Reached Route

- Use condition check in update loop: enemy `y > 110`.
- Destroy enemy and reduce life.
- Ensure one life loss per enemy event.

# Slide 6: Build Checkpoint

- Start with `info.setLife(3)`.
- Test 3 failed defences.
- Confirm game ends when life hits 0.

# Slide 7: Level 1-4 Task Choices

- Level 1: Implement one lose-condition method (collision or bottom).
- Level 2: Implement both methods.
- Level 3: Add clear on-screen warning when player loses a life.
- Level 4: Add continue/restart flow and justify the design.

# Slide 8: Plenary / Exit Question

- Which lose condition creates better gameplay tension and why?

# Slide 9: Homework / Extension

- Design a game-over screen message set (fail, retry, high-score prompt).
