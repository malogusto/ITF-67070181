const username = document.getElementById("username")
const inputUsername = document.getElementById("inputUsername")
const inputImage = document.getElementById("inputImage")
const image = document.getElementById("profile")
let count = 1
function setUsername() {
    username.textContent = inputUsername.value
    inputUsername.value = ""
}
function setImage() {
    image.style.backgroundImage = "url(" + inputImage.value + ")"
}
function addName() {
    const usertel = document.getElementById("inputName").value;
    const tel = document.getElementById("inputPhone").value;

    if (usertel && tel) {
        const newRow = document.createElement("tr");
        const tdNum = document.createElement("td");
        tdNum.textContent = count++;
        const tdName = document.createElement("td");
        tdName.textContent = usertel;
        const tdPhone = document.createElement("td");
        tdPhone.textContent = tel;
        newRow.appendChild(tdNum);
        newRow.appendChild(tdName);
        newRow.appendChild(tdPhone);
        document.getElementById("create").appendChild(newRow);
        document.getElementById("inputName").value = "";
        document.getElementById("inputPhone").value = "";
    }
}
function saveCSV() {
    let phonenumber = [];
    let table = document.getElementById("create");
    let rows = table.querySelectorAll("tr");
    rows.forEach(row => {
        let cols = row.querySelectorAll("th, td");
        let rowContent = [];
        cols.forEach(col => rowContent.push(col.textContent.trim()));
        phonenumber.push(rowContent);
    });
    const csvContent = phonenumber.map(row => row.join(",")).join("\n");
    const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
    const link = document.createElement("a");
    const url = URL.createObjectURL(blob);
    link.setAttribute("href", url);
    link.setAttribute("download", "data.csv");
    link.style.visibility = "hidden";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}