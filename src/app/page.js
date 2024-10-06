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
      <h2 className={styles.testButtonHeader}>{heading}</h2>
      {testlist.map((test) => (
        <button key={test.id} className={styles.testButton} onClick={() => onswitchTest(test)}>
          <p className={styles.testButtonText}>{test.name}</p>
        </button>
      ))}
    </>
  );
}

function TestViewer({test}){
  var feedback = "Submit your test for feedback";
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
        <div className={styles.testContainer}>
          <iframe src = {test.path} className={styles.frame}></iframe>
          <div className={styles.feedbackContainer}>
            <div className={styles.feedback}>
              <h2 className={styles.feedbackTitle}>
                Feedback
              </h2>
              <div className={styles.feedbackTextContainer}>
                <p>{feedback}</p>
              </div>
              <div className={styles.testUpload}>
                <h3>Upload File</h3>
                <form method="post" encType="multipart/form-data">
                  <input type="file" name="file" />
                  <input type="submit" value="Upload" />
                </form>
              </div>
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