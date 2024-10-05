'use client'
import styles from "./page.module.css";
import React from 'react';

class TestObj {
  constructor(name, author) {
      this.name = name;
      this.author = author;
  }
}

function TestModuleButtonList({testlist}){
  const count = testlist.length; 
  let heading = "";
  if (count > 0) {
    const noun = count > 1 ? 'Tests' : 'Test';
    heading = count + ' ' + noun;
  }
  return (
    <>
      <h2>{heading}</h2>
      {testlist.map(test =>
        <button className={styles.testButton}>
          {test.name}
        </button>
      )}
    </>
  );
}

export default function Home() {
  let Tests = [];
  let obj1 = new TestObj("Gay", "Preetham");
  let obj2 = new TestObj("Gay", "Preetham");
  let obj3 = new TestObj("Gay", "Preetham");
  let obj4 = new TestObj("Gay", "Preetham");
  Tests.push(obj1);
  Tests.push(obj2);
  Tests.push(obj3);
  Tests.push(obj4);
  return (
    <>
    <div className={styles.MainGrid}>
      <div className={styles.NavBar}>
        <p className={styles.logo}>LOGO</p>
      <TestModuleButtonList className={styles.testButtonList} testlist = {Tests}/>
      </div>
      <div className={styles.content}>
        <header className={styles.title}>K-12 APP</header>
      </div>
    </div>
    </>
  );
}