import Check from "./Check";
import { BsTrash } from "react-icons/bs";

interface Todo {
  id: number;
  title: string;
  isCompleted: boolean;
}

interface TodoItemProps {
  todo: Todo;
  changeTodo: (id: number) => void;
  removeTodo: (id: number) => void;
}

const TodoItem: React.FC<TodoItemProps> = ({
  todo,
  changeTodo,
  removeTodo,
}: TodoItemProps) => {
  return (
    <div className="flex items-center justify-between mb-4 bg-gray-600 rounded-xl p-5">
      <button className="flex items-center" onClick={() => changeTodo(todo.id)}>
        <Check isCompleted={todo.isCompleted} />
        <span className={`${todo.isCompleted ? "line-through" : ""}`}>
          {todo.title}
        </span>
      </button>
      <button onClick={() => removeTodo(todo.id)}>
        <BsTrash
          className="text-gray-700 hover:text-red-600 transition-colors"
          size={22}
        />
      </button>
    </div>
  );
};

export default TodoItem;
