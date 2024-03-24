const btnEl = document.getElementById('btn');
const appEl = document.getElementById('app')

function deleteNote(){
    
}

function updateNote(){

}

function createNodeEl(id, content){
    const element = document.createElement("textarea")
    element.classList.add("note")
    element.placeholder = "Element Note"
    element.value = content

    element.addEventListener("dblclick", ()=>{
        const warning = confirm("Do you want to Delete this Note ?")
        if(warning){
            deleteNote(id. element)
        }
    })

    element.addEventListener("input", ()=>{
        updateNote(id, element.value)
    })

    return element;
}


function addNote(){
    // console.log("Clicked")
    const notes = getNotes();
    const noteObj = {
        id :Math.round(Math.random() * 100000),
        content : ""
    };

    const noteEl = createNodeEl(noteObj.id, noteObj.content)

    appEl.insertBefore(noteEl, btnEl);
    notes.push(noteObj);

    saveNotes(notes);
}

function saveNotes(notes){
    localStorage.setItem("note-app", JSON.stringify(notes))

}

function getNotes(){
    return JSON.parse(localStorage.getItem("note-app") || "[]");
}

btnEl.addEventListener("click", addNote);

