
function merge_sort(list = Array){
    let len = list.length;
    if (len <= 1){
        return list
    }
    let mid = Math.floor(len/2);
    let left = merge_sort(list.slice(0,mid));
    let right = merge_sort(list.slice(mid));
    let final = [];
    while (left.length > 0 && right.length > 0){
        if(left[0]<right[0]){
            final.push(left.shift())
        }else{
            final.push(right.shift())
        }
    };
    
    return final.concat(left).concat(right)
}
