Repo for 2025 Advent of Code

I used the 2024 AoC to learn Python -- for 2025 I want to refresh and improve my knowledge.

https://adventofcode.com/2025

Interestingly, way back when I did 2024, I used AI a lot to teach me Python (not to actually write the solutions though). Now a little over a year later I am deliberately not using AI at all, although I am referencing my 2024 work a lot to help with Python since I haven't written any since then. I don't write code at work anymore (I tell an agent what to write) so I'm using this as an opportunity to flex that muscle, thus the resistance to using AI. Strange how quickly things change.

## Usage

```
py -m day[n].main[1,2]
```

## Summaries

### Day 1
Part 1 easy to solve with mod, and Part 2 seemed easy with integer division, but I had a few troublesome corner cases. Finally I wrote some tests to visualize the issue easier and some clumsy code to adjust the result. I bet there's a cooler way to do it mathematically without the clumsy if, but good enough!

### Day 2
Part 1 was pretty straightforward, no surprises. Those always have the best part 2 that makes me chuckle, and this one is no execption. Part 2 actually didn't end up being too bad either -- I was expecting to need to come up with a clever optimization. But a simple naive approach with some long-hanging optimizations did the trick, with a notable slow execution of around 5-10 seconds.