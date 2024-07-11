document.getElementById("empform").addEventListener("submit",async(e)=>{
    e.preventDefault();
    const fname = document.getElementById("first_name").value;
    const lname = document.getElementById("last_name").value;
    const sal= document.getElementById("salary").value;
    const dept = document.getElementById("dept").value;
    const role = document.getElementById("role").value;
    const bonus = document.getElementById("bonus").value;
    const phno = document.getElementById("phone").value;
    console.log(fname)
    const resData = await fetch("http://127.0.0.1:8000/add_emp",{
    method:"POST",
    body:JSON.stringify({
    first_name:fname,
    last_name:lname,
    salary:sal,
    dept:dept,
    role:role,
    bonus:bonus,
    phone:phno}),
    headers:{"Content-type":"application/json; charset=UTF-8"}
    });
    if(resData.status===200){
        alert("Employee Added Successfully")
        e.target.reset()
    }

})