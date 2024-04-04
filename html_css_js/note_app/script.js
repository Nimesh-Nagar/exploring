const btnEl = document.getElementById('btn');
const appEl = document.getElementById('app');

getNotes().forEach((note)=>{
    const noteEl = createNoteEl(note.id, note.content);
    appEl.insertBefore(noteEl, btnEl);
});

function deleteNote(id , element ){
    const notes = getNotes().filter((note)=>note.id != id);
    saveNotes(notes)
    appEl.removeChild(element)
    
}

function updateNote(id, content){
    const notes = getNotes();
    const target = notes.filter((note)=> note.id == id)[0];
    target.content = content;
    saveNotes(notes); 


}

function createNoteEl(id, content){
    const element = document.createElement("textarea")
    element.classList.add("note")
    element.placeholder = "Element Note"
    element.value = content

    element.addEventListener("dblclick", ()=>{
        const warning = confirm("Do you want to Delete this Note ?")
        if(warning){
            deleteNote(id, element)
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

    const noteEl = createNoteEl(noteObj.id, noteObj.content)

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

