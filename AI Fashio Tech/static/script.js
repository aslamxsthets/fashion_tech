async function generate(){

const gender=document.getElementById("gender").value;
const occasion=document.getElementById("occasion").value;
const color=document.getElementById("color").value;
const style=document.getElementById("style").value;

const res=await fetch("/recommend",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({gender,occasion,color,style})
});

const data=await res.json();

document.getElementById("output").innerText=data.result;
document.getElementById("trend").innerText="🔥 Trend: "+data.trend;
}