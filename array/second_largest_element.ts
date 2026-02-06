function secondHighest(s: string): number {
	if (s.length < 2) {
		return -1;
	}

	let first: number = -Infinity;
	let second: number = -Infinity;

	for (const c of s) {
		const num = parseInt(c);
		if (Number.isNaN(num)) {
			continue;
		}

		if (num > first) {
			second = first;
			first = num;
		} else if (num > second) {
			second = num;
		}
	}

	return second === -Infinity ? -1 : second;
}

console.log(secondHighest("dfa12321afd"));
// console.log('HIiii')