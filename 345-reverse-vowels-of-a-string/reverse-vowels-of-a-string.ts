function reverseVowels(s: string): string {
    const vowels: string = "aeiouAEIOU";
    let ch: string[] = s.split("");
    let low = 0,
        high = s.length - 1;
    while (low < high) {
        if (vowels.includes(ch[low]) && vowels.includes(ch[high])) {
            [ch[low], ch[high]] = [ch[high], ch[low]];
            low++, high--;
        }
       else if (!vowels.includes(ch[low])) low++;
       else if (!vowels.includes(ch[high])) high--;
    }
    return ch.join("");
};