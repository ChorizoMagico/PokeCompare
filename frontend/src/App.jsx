import './App.css'

function App(){

  return (
  <div>


    <div className="main-grid"> 

      <h1 className="title"> TeamCompare </h1>

      <div className="top-grid"> 
        <h2 className="nombre-equipo"> Nombre </h2>
        <h2 className="cantidad-equipos"> i/n </h2>
      </div>

      <div className="medium-grid"> 
        <button className="boton-opciones"> Opciones </button>
        <button className="boton-comparar"> Comparar </button>
      </div>

      <div className="bottom-grid"> 
        <h2 className="nombre-usuario"> Nombre </h2>
        <h2 className="barra-pokemones"> Pokemones </h2>
      </div>

    </div>
    
  </div>

)}

export default App