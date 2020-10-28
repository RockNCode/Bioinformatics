// 1. Code runs as you type: edit message
let msg = 'hello world'
let str1 = "CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG"
let str2 = "ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"
let skewStr = "GATACACTTCCCGAGTAGGTACTG"

let strForCount = "TACGCATTACAAAGCACA"
let countPattern = "AA" // with one mutation
let countRes = 0;


let haming = 0;

var skew = 0;
var maxSkew = 0;
var skewMaxIndex = -1

var minSkew = 1000;
var skewMinIndex = -1


for(var i = 0 ;i < (strForCount.length-1); i++){
  var mCount =0;
  for(var j = 0; j < countPattern.length;j++){
    mCount += countPattern[j] == strForCount[i+j];
  }
  console.log(mCount)
  if(mCount >= (countPattern.length-1))
    countRes+=1
}


for(var i = 0 ;i < str1.length; i++){
  haming += str1[i] == str2[i] ? 0 : 1
}

for(var i = 0 ;i < skewStr.length; i++){
  var countG =0;
  var countC =0;
  for(var j = 0; j < i; j++) {
    countG+= skewStr[j] =="G" ? 1 : 0
    countC+= skewStr[j] =="C" ? 1 : 0

  }
  skew = countG - countC

  if(skew > maxSkew) {
    skewMaxIndex = i
    maxSkew = skew
  }
  if(skew < minSkew) {
    skewMinIndex = i
    minSkew = skew
  }
  skew=0;
}

console.log("max index of skew is " + skewMaxIndex +" where skew was " + maxSkew + " haming : " + haming + " Count() result : "+ countRes)
console.log("Min skew : " + minSkew  + " Min index : " +skewMinIndex)
