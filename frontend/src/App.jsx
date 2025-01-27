import React, { useState, useEffect } from "react";

const App = () => {
  // data is the actual variable, and setData is a function we can use to
  // manipulate the Data variable.
  const [data, setData] = useState([]);

  useEffect(() => {
    fetch("/members")
      .then((res) => res.json())
      .then((data) => {
        setData(data);
        console.log(data);
      });
  }, []);
  return <div>App</div>;
};

export default App;
