import './App.css';
import LevelView from './components/level/LevelView';

function App() {
  return (
    <div className="App">
      <LevelView level={1} />
      <LevelView level={1} />
    </div>
  );
}

export default App;
