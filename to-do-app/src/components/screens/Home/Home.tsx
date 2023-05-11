import { useState } from "react";
import TodoItem from "./item/TodoItem";
import TodoInput from "./item/Todoinput";
const data = [
  {
    id: 1,
    title: "Finish frontend task",
    isCompleted: false,
  },
  {
    id: 2,
    title: "Read the book",
    isCompleted: false,
  },
  {
    id: 3,
    title: "Cook dinner",
    isCompleted: false,
  },
];
const Home: React.FC = () => {
  const [todos, setTodos] = useState(data);
  const changeTodo = (id: number) => {
    const copy = [...todos];
    const current = copy.find((t) => t.id === id);
    if (current) {
      current.isCompleted = !current.isCompleted;
      setTodos(copy);
    }
  };
  const removeTodo = (id: number) => {
    setTodos(todos.filter((t) => t.id !== id));
  };
  const addTodo = (title: string) => {
    setTodos([
      {
        id: Date.now(),
        title,
        isCompleted: false,
      },
      ...todos,
    ]);
  };
  return (
    <div className="text-white w-4/5 mx-auto">
      <h1 className="text-2xl font-bold text-center mb-8">My Todo List</h1>
      {todos.map((todo) => (
        <TodoItem
          key={todo.id}
          todo={todo}
          changeTodo={changeTodo}
          removeTodo={removeTodo}
        ></TodoItem>
      ))}
      <TodoInput addTodo={addTodo}></TodoInput>
    </div>
  );
};

export default Home;
