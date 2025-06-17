const runningSum = (nums)=> {
    const outputArray=[]
    let sum=0;
    nums.forEach(value=>{
        sum+=value;
        outputArray.push(sum);
    })
    return outputArray;
};