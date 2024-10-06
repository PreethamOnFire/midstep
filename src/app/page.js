'use client'
import styles from "./page.module.css";
import React from 'react';
import {Tests,TestObj} from "./Links"
import Image from "next/image";
import appName from './Midstep.png';


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
      <div className={styles.testVeiwerContainer}>
        <div className={styles.testTitleContainer}>
          <h1 className={styles.testTitle}>
            {test.name}
          </h1>
          <h2 className={styles.author}>
            {test.author}
          </h2>
        </div>
        <div>
          <h1>Upload File</h1>
          {/* <form onSubmit={handleSubmit} method="post" encType="multipart/form-data">
            <input type="file" name="file" />
            <input type="submit" value="Upload" />
          </form> */}
        </div>
        <div className={styles.testContainer}>
          <iframe src = "https://en.wikipedia.org/wiki/Wikipedia" className={styles.frame}></iframe>
          <div className={styles.feedbackContainer}>
            <div className={styles.feedback}>

            </div>
          </div>
        </div>
        <div className={styles.tagContainer}>
          <div classname={styles.tags}>

          </div>
        </div>
        
      </div>
    </>
  );
}

export default function Home() {
  const [content, setContent] = React.useState("");
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
          <header className={styles.title}><Image src={appName} alt="Midstep" width={400} height={200}/></header>
        </div>
        {content}
      </div>
    </div>
    </>
  );
}