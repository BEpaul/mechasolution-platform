import logo from './logo.svg';
import './App.css';

function Header(props){
  console.log('props', props, props.title);
  return <header>
    <h1><a href="/">{props.title}</a></h1>
  </header>
}
function Nav(props){

  const lis = [];
  for(let i=0; i<props.topics.length; i++){
    let t = props.topics[i];
  lis.push(<li key={t.id}><a href={'/read/' + t.id}>{t.title}</a></li>)
    
  }

  return <nav>
    <ol>
      {lis}
    </ol>
  </nav>
}
function Article(props){
  return <article><h2>{props.title}</h2>
  {props.body}
  </article>
}
function App() {
  const topics = [
    {id:1, title:'html', body:'html is ...'},
    {id:2, title:'css', body:'css is ...'},
    {id:3, title:'javascript', body:'javascript is ...'}
  ] 
  return (
    <div className="App">
      <Header title="REACT"></Header>
      <Nav topics={topics}></Nav>
      <Article title="Welcome" body="Hello, WEB"></Article>

      {/* <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header> */}
    </div>
  );
}

export default App;
