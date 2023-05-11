type Props = {
  children?: React.ReactNode;
};
const Layout: React.FC<Props> = ({ children }) => {
  return <div className="py-10 bg-gray-700 h-screen">{children}</div>;
};

export default Layout;
