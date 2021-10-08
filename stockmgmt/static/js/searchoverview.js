const searchField = document.querySelector("#searchField");
const tableOutput = document.querySelector("#table-output");
const appTable = document.querySelector(".app-table");
const itemNotFound = document.querySelector(".item-not-found");
const tbody = document.querySelector(".table-body")
tableOutput.style.display='none';
itemNotFound.style.display='none';

searchField.addEventListener("keyup",(e) =>{
    const searchValue = e.target.value;
    console.log(searchValue);

    if(searchValue.trim().length > 0) {
        itemNotFound.style.display="none";
        tbody.innerHTML="";
        fetch("search_in_overview",{
            body: JSON.stringify({ searchText : searchValue }),
            method: "POST"
        })
        .then((res) => res.json())
        .then((data) => {
            console.log("data", data)
            appTable.style.display='none'
            tableOutput.style.display='block'

            if (data.length === 0){
                itemNotFound.style.display="block"
                tableOutput.style.display='none'
            }
            else{
                data.forEach((item) => {
                    if(item.operation==="receipt"){
                        tbody.innerHTML += `
                        <tr class="table-success">
                        <td>${item.operation}</td>
                        <td>${item.date}</td>
                        <td>${item.description}</td>
                        <td>${item.wheat}</td>
                        <td>${item.rice}</td>
                        <td>${item.combo}</td>
                        </tr>`;
                    }
                    else if(item.operation==="consumption"){
                        tbody.innerHTML += `
                        <tr class="table-danger">
                        <td>${item.operation}</td>
                        <td>${item.date}</td>
                        <td>${item.description}</td>
                        <td>${item.wheat}</td>
                        <td>${item.rice}</td>
                        <td>${item.combo}</td>
                        </tr>`;
                    }
                });
            }


        });


    }

    else{
        appTable.style.display='block';
        tableOutput.style.display='none';
    }

});