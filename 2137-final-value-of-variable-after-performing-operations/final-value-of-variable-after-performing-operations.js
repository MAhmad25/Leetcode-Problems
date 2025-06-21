const finalValueAfterOperations = function(operations) {
    let X=0;
    operations.forEach(op=>{
        if(op==="--X"||op==="X--" )
        X--;
        else if(op==="++X"||op==="X++" )
        X++;
    })
    return X;
};