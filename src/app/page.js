'use client'
import styles from "./page.module.css";
import React from 'react';
import {Tests,TestObj} from "./Links"


function TestModuleButtonList({testlist, onswitchTest}) {
  const count = testlist.length; 
  let heading = "";
  if (count > 0) {
    const noun = count > 1 ? 'Tests' : 'Test';
    heading = `${count} ${noun}`;
  }

  return (
    <>
      <h2>{heading}</h2>
      {testlist.map((test) => (
        <button key={test.id} className={styles.testButton} onClick={() => onswitchTest(test)}>
          <p>{test.name}</p>
        </button>
      ))}
    </>
  );
}

function TestViewer({test}){
  return(
    <>
    <div className={styles.testTitleContainer}>
      <h1 className={styles.testTitle}>
        {test.name}
      </h1>
    </div>
    <h2 className={styles.author}>
      {test.author}
    </h2>
    </>
  );
}

export default function Home() {
  const [content, setContent] = React.useState("Welcome to MidStep!");
  function switchTest(test) {
    return (setContent(<TestViewer test={test} />)); // Pass the test object directly
  }
  return (
    <>
    <div className={styles.MainGrid}>
      <div className={styles.NavBar}>
        <img src='/logo.ico' alt='logo'/>
        <TestModuleButtonList className={styles.testButtonList} testlist={Tests} onswitchTest={switchTest}/>
      </div>
      <div className={styles.content}>
        <div className={styles.titleContainer}>
          <header className={styles.title}>K-12 APP</header>
        </div>
        {content}
      </div>
    </div>
    </>
  );
}