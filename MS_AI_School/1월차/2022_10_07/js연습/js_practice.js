// #1-----------------------------------------------------
function sum(array)  {
    let result=0
    for(let i=0; i<array.length; i++){
        result +=array[i]
    }
    return result
}

let numbers_1 = [10,20,30]
let result_1 = sum(numbers_1)
console.log(result_1)

// #2-----------------------------------------------------
function isEven(num){
    if(num%2==0){
        return true
    } else {
        return false
    }
}

let numbers_2 = 2
let result_2 = isEven(numbers_2)
console.log(result_2)

// #3-----------------------------------------------------
function isOdd(num){
    if(num%2 == 1){
        return true
    } else {
        return false
    }
}

let numbers_3 = 1
let result_3 = isOdd(numbers_3)
console.log(result_3)

// #4-----------------------------------------------------
function evenSum(array){
    let result = 0
    for(let i=0; i<array.length; i++){
        if (array[i]%2 == 0){
            result+=array[i]
        } else{
            continue
        }
    }
    return result
}

let numbers_4 = [10,21,30]
let result_4 = evenSum(numbers_4)
console.log(result_4)

// #5-----------------------------------------------------
function objectSum(numO){
    let result = 0
    for(let i=0; i<numO.length; i++){
        if(numO[i]['number']%2 == 1) {
            result+=numO[i]['number']
        } else {
            continue
        }
    }
    return result
}

let numObject = [{'name':'lee','number':22},{'name':'park','number':11}]
let result_5 = objectSum(numObject)
console.log(result_5)

// #6-----------------------------------------------------
function totalSum(n){
    let result=0
    for(let i=n; i>0; i--){
        result+=i
    }
    return result
}

let num_6 =11
let result_6 =totalSum(num_6)
console.log(result_6)

// #7-----------------------------------------------------
function countKorean(array){
    let cnt=0
    for(let i=0; i<array.length; i++){
        if(array[i]=='국어'){
            cnt+=1
        } else {
            continue
        }
    }
    return cnt
}

let subs_7 = ['국어','수학','영어','국어','과학']
let result_7 = countKorean(subs)
console.log(result_7)

// #8-----------------------------------------------------
function countSubject(subject,array){
    let cnt=0
    for(let i=0; i<array.length; i++){
        if(subject==array[i]){
            cnt+=1
        } else {
            continue
        }
    }
    return cnt
}

let subs_8=['국어','수학','영어','국어','과학']
let result_8 = countSubject('수학',subs_8)
console.log(result_8)

// #9-----------------------------------------------------
function countGrade(array){
    let cnt =0
    for(let i=0; i<array.length; i++){
        if(array[i]>=90){
            cnt+=1
        }else{
            continue
        }
    }
    return cnt
}

let grads_9 = [90,82,100,70,80]
let result_9 = countGrade(grads_9)
console.log(result_9)

// #10-----------------------------------------------------
function avg(array){
    let add=0, cnt=0
    for(let i=0; i<array.length; i++){
        if(array[i]>=90){
            add+=array[i]
            cnt+=1
        }else{
            continue
        }
    }
    return add/cnt
}

let grads_10 = [90,82,100,70,80]
let result_10 = countGrade(grads_10)
console.log(result_10)