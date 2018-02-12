var page_url = "127.0.0.1:8000";


   
fetch(`http://${page_url}/all`)
.then(res => {
    res.json()
    .then((data) => {
        console.log(data)
        moremi(data)
    }).then(()=>{
        console.log("njksdnskdn")
    })
})


// //var image_array     = []
// setTimeout(() => {
   
// }, 2000);