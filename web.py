import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo_local = st.session_state["new_todo"] + "\n"
    todos.append(new_todo_local)
    functions.write_todos(todos)

st.title("My Todo App!")
st.subheader("This app is designed to increase your productivity!"
             " (Or not, who cares for a low-life like you?)")
st.write("List of todos below, bitch:")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="Enter todo, lil bitch", placeholder="Add a todo, moron",
              on_change=add_todo, key="new_todo")