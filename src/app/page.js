'use client'
import styles from "./page.module.css";
import React from 'react';


export default function Home() {
  return (
    <>
    <div className={styles.MainGrid}>
      <div className={styles.NavBar}>
        <p className={styles.logo}>LOGO</p>
        <button className={styles.color}>Test 1</button>
      </div>
      <div className={styles.content}>
        <header className={styles.title}>K-12 APP</header>
      </div>
    </div>
    </>
  );
}