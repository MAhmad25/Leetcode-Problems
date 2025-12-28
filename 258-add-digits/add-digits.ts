function addDigits(num: number): number {
    while (num >= 10) {
        let quotient: number = Math.floor(num / 10);
        let remainder: number = num % 10;
        num = quotient + remainder;
    }
    return num;
}