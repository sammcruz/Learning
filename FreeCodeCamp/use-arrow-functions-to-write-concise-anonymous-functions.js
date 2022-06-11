const magic = () => {
  const magic = new Date();
  return magic
};

const magic2 = () => new Date() ;

console.log(magic())
console.log(magic2())