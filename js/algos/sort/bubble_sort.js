const bubbleSort = lst => {
    for(let endPtr=lst.length() - 1; endPtr >= 0; endPtr--){
        for(let i=0; i<endPtr; i++){
            if(lst[i] > lst[i+1]){
                const temp = lst[i];
                lst[i] = lst[i+1];
                lst[i+1] = temp;
            }
        }
    }
    return lst;
}

export default bubbleSort;

