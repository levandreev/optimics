import { BsCheck } from "react-icons/bs";
interface CheckItemProps {
  isCompleted: boolean;
}
const Check = ({ isCompleted }: CheckItemProps) => {
  return (
    <div className={`border-2 rounded-lg border-pink-300 w-6 h-6 mr-3 ${isCompleted ? 'bg-pink-300' : ''} flex items-center justify-center`}>
      {isCompleted && <BsCheck size={24} className="text-gray-900" />}
    </div>
  );
};

export default Check;
