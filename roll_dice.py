from tqdm import tqdm
import random
import time

class DiceExperiment:
    def __init__(self):
        self.dices = [1, 1]

    def _roll_dice(self):
        self.dices = [random.randint(1, 6) for _ in range(2)]
        return self.dices

    def run(self):
        die1, die2 = self._roll_dice()
        return die1 + die2

def main():
    NUM_TRIALS = 100_000_000
    count_sum_7 = 0
    experiment = DiceExperiment()

    start_time = time.time()
    for _ in tqdm(range(NUM_TRIALS)):
        total = experiment.run()
        if total == 7:
            count_sum_7 += 1
    end_time = time.time()

    probability = count_sum_7 / NUM_TRIALS
    print(f"Ran run_experiment() {NUM_TRIALS:,} times.")
    print(f"Number of times sum = 7: {count_sum_7:,}")
    print(f"Estimated probability of sum = 7: {probability:.6f}")
    print(f"Elapsed time: {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    main()