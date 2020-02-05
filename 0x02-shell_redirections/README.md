The following README describes the commands used for the 0x02-shell_redirections at Holberton's school.

0. Hello World --> echo "Hello, World"
1. Confused smiley --> echo "\"(Ôo)'" 
2. Let's display a file --> cat /etc/passwd
3. What about 2? --> cat /etc/passwd /etc/hosts
4. Last lines of a file --> tail -n 10 /etc/passwd
5. I'd prefer the first ones actually --> head -n 10 /etc/passwd
6. Line #2 --> head -3 iacta | tail -1
7. It is a good file that cuts iron without making a noise --> echo "Holberton School" > "\*\\\'\"Holberton School\"\'\\\*$\?\*\*\*\*\*:)" 
8. Save current state of directory --> ls -la > ls_cwd_content
9. Duplicate last line --> tail -1 iacta >> iacta
10. No more javascript --> find . -name "*.js" -type f -delete
11. Don't just count your directories, make your directories count --> ls -lR | grep "^d" | wc -l 
12. What’s new --> ls -Ut | head -10
13. Being unique is better than being perfect --> sort | uniq -u
14. It must be in that file --> grep "root" /etc/passwd
15. Count that word --> grep -c "bin" /etc/passwd
16. What's next? --> grep -A 3 "root" /etc/passwd
17. I hate bins --> grep -v "bin" /etc/passwd
18. Letters only please --> grep -i ^[a-z] /etc/ssh/sshd_config
19. A to Z --> tr 'Ac' 'Ze'
20. Without C, you would live in hiago --> tr -d 'Cc'
21. esreveR --> rev
22. DJ Cut Killer --> cut -d: -f1,6 /etc/passwd | sort
23. Empty casks make the most noise --> find . -empty |rev | cut --delimiter='/' -f1 | rev
24. A gif is worth ten thousand words --> find  -name "*gif" -type f -printf "%f\n" | rev | cut -c 5- | rev | LC_ALL=C sort -f
25. Acrostic --> cut -c 1 | tr -d [:space:] | xargs -r
26. The biggest fan --> tail -n+2 | cut -f1 | sort | uniq -c | sort -nr | rev |  cut --delimiter=' ' -f1 | rev | head --lines=11

