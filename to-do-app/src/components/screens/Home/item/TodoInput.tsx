import { useState } from "react";

interface Props {
  addTodo: (title: string) => void;
}
const TodoInput = ({ addTodo }: Props) => {
  const [title, setTitle] = useState("");

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    addTodo(title);
    setTitle('');
  };
  return (
    <div className="flex items-center justify-between mb-4 bg-gray-600 rounded-xl px-5 py-2 mt-20 w-full">
      <form onSubmit={handleSubmit}>
        <input
          className="bg-transparent w-full border-none outline-none"
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Add a task"
        ></input>
      </form>
    </div>
  );
};

export default TodoInput;
