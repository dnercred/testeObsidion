
## Descrição do projeto

# teclado

Assuma o controle total do seu teclado com esta pequena biblioteca Python. Conecte eventos globais, registre teclas de atalho, simule o pressionamento de teclas e muito mais.

## Características

- **Gancho de evento global** em todos os teclados (captura teclas independentemente do foco).
- **Ouça** e **envie** eventos de teclado.
- Funciona com **Windows** e **Linux** (requer sudo), com suporte experimental **para OS X (obrigado @glitchassassin!).**
- **Python puro** , sem módulos C a serem compilados.
- **Zero dependências** . Trivial para instalar e implantar, basta copiar os arquivos.
- **Pitão 2 e 3** .
- Suporte complexo a teclas de atalho (por exemplo `ctrl+shift+m, ctrl+space`) com tempo limite controlável.
- Inclui **API de alto nível** (por exemplo, [record](https://pypi.org/project/keyboard/#keyboard.record) and [play](https://pypi.org/project/keyboard/#keyboard.play) , [add_abbreviation](https://pypi.org/project/keyboard/#keyboard.add_abbreviation) ).
- Mapeia as chaves como elas realmente estão no seu layout, com **suporte total à internacionalização** (por exemplo `Ctrl+ç`, ).
- Eventos capturados automaticamente em thread separado, não bloqueiam o programa principal.
- Testado e documentado.
- Não quebra teclas mortas acentuadas (estou olhando para você, pyHook).
- Suporte a mouse disponível através do [mouse](https://github.com/boppreh/mouse) do projeto ( `pip install mouse`).

## Uso

Instale o [pacote PyPI](https://pypi.python.org/pypi/keyboard/) :

```
pip install keyboard
```


### Exemplo 
```python
import keyboard

keyboard.press_and_release('shift+s, space')

keyboard.write('Familia DIB.')

keyboard.add_hotkey('ctrl+shift+a', print, args=('triggered', 'hotkey'))

# Pressione PAGE UP e depois PAGE DOWN para digitar "foobar".
keyboard.add_hotkey('page up, page down', lambda: keyboard.write('foobar'))

# Bloqueia até pressionar esc.
keyboard.wait('esc')

# Record events until 'esc' is pressed.
# Grave eventos até que 'esc' seja pressionado.
recorded = keyboard.record(until='esc')
# Then replay back at three times the speed.
# Em seguida, reproduza o triplo da velocidade.
keyboard.play(recorded, speed_factor=3)

# Type @@ then press space to replace with abbreviation.
# Digite @@ e pressione espaço para substituir por abreviação.
keyboard.add_abbreviation('@@', 'my.long.email@example.com')

# Block forever, like `while True`.
# Bloquear para sempre, como 'enquanto True'.
keyboard.wait()




```





[https://github.com/mhinz/vim-startify](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbHBQeGFEV2VlcnRuT1AySXVYZGhqVTM2Wl9jZ3xBQ3Jtc0trcmwtMDdZYzRrZEFHbnJCbDVnajhndU9rMXlOSVh5TjZrLXhPaU03Um8xRnBLQ0VYNVNrcm9SSjIwSHVtSGNPckFVZEFLN21Gd2w5Tmc0TlVTSWx4LTBIaGZkTGxUaDFLcURUZ1BXWkd0OENEUnJBMA&q=https%3A%2F%2Fgithub.com%2Fmhinz%2Fvim-startify&v=hdZMqMeruSQ) [https://github.com/rafi/awesome-vim-c...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbThvazNaZ2VnNmNWajFfR21jcHN4SloyOVJaZ3xBQ3Jtc0tuWVVTSnpRbXFITlVUNHVkZ0hDNC1RZUozeVNYeXhPQVJYREpHQWFFZXkzOWYteWJEVnFNZUIxcnJrb3E4RWI2Vnp4YlYwMVlzQjgyVTRMWXJ2LUxrMFFtZ0xpTVdoMk4xeTRmRFJYWWNJaEF6VlRNQQ&q=https%3A%2F%2Fgithub.com%2Frafi%2Fawesome-vim-colorschemes&v=hdZMqMeruSQ) [https://github.com/tomasiser/vim-code...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbVpDekZDY21tUFFUc05RdE9QcklRR0E4ZC1ad3xBQ3Jtc0tsMEliMnBneEpaZXYyYXVNNkRQbWR4MjFRS1YzX0ZOQThtc2dUNUNrTEtzUk9JR2xRbl85NGFVMVd0V0ZEOXRYaWM0ejBUb0xQaERFX08tVTFqMlMzajhRMG1CQUg5Ylh0V0pQUnRiUG1EOTljZUM0WQ&q=https%3A%2F%2Fgithub.com%2Ftomasiser%2Fvim-code-dark&v=hdZMqMeruSQ) [https://github.com/Yggdroot/indentLine](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbmJjQ2dxeVFOMFFfQzd6TjBDanNrd0hqOUZkUXxBQ3Jtc0ttdXVBckRkc3VZblpWcnFWZ0QzUW44S2NuV0F1N1dyZkh3OGhTYldxc1I1bFlYLWd4YjQyRDlTZUxPT1lnOUxBYmFuMmFISEJPeFNMclN1bGhYLS1yb1pZX3c2dkVPUGk1azBaTDI0bUxhTEVCejZOMA&q=https%3A%2F%2Fgithub.com%2FYggdroot%2FindentLine&v=hdZMqMeruSQ) [https://github.com/preservim/nerdtree](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbFRURFJRLTExZUx4UWxoQ3V4ZkpnZS1SLV9rd3xBQ3Jtc0trVFY0eUpQazktUEw0WjY3WXZ6aWVLeEkzNEFFTjgyOUhKZ25hSGluV09tb1FLWGowSEgzMU44czBvZ0NKMEhpREJXaXQ0VFFrSXBWbzdncGV3X001X2pYSmJ2M055U3A5ZENJSzl3ZlgxVU5xUGVvVQ&q=https%3A%2F%2Fgithub.com%2Fpreservim%2Fnerdtree&v=hdZMqMeruSQ) [https://github.com/ryanoasis/vim-devi...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbFJ5eEdXbWd6ZjVPQjZFSnFIQ3MtNFEyVUJwZ3xBQ3Jtc0tsd1NUSkQ3cERsalhfV1RvZV90RnQ1WVhZYlRDUkduVEZ6MU9HNVNyZDR0VWFrbk9qa2JIT1g2b283ZmZtQzczOFE3ZlJTTkJHcll5SkFkYmZuMVRIb2MxTXoyY3lBWERPd0I2YWFTN2lfa2dza1R0RQ&q=https%3A%2F%2Fgithub.com%2Fryanoasis%2Fvim-devicons&v=hdZMqMeruSQ) [https://github.com/vim-airline/vim-ai...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbUt6bndlT3prR1pBSUczN2pRcm03eEx4R2RnZ3xBQ3Jtc0tuRm9wcUdibHd5cFNRaGJuYmNpdE1GLWIxeXNQdFRFY0hvN3N1Y084THRVM0MzaVRoZWJBUDN5bXVyanV5QS10RlFpbE15WTRmR3JSU3JGYUpVRktncnFQU09kSVZ4a1I5aGpMZkphNDhzbkZlN3dSTQ&q=https%3A%2F%2Fgithub.com%2Fvim-airline%2Fvim-airline&v=hdZMqMeruSQ) [https://github.com/vim-airline/vim-ai...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbEtUQjhaaVBSQkJ2R3NWSDJ5MXU4X2ptNUU5d3xBQ3Jtc0trZmdiVUtrUDEyb0txZ0VYZjExT0tiLTE2dDI0Ymd1OG1Ec3QzVDU1UjRnYkhMZ3pmbzFMNGt6VkhTUXZNYlZUMmlqQThybjg0RFQxZ2NFN25scGJTOFRSOUM0LTVDakg2M1RhSGI4OEV5dGk3UGMySQ&q=https%3A%2F%2Fgithub.com%2Fvim-airline%2Fvim-airline-themes&v=hdZMqMeruSQ) [https://github.com/ctrlpvim/ctrlp.vim](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqazlnREg1b2F6dU91UGJGQk0xTUE1TUR5RXdXd3xBQ3Jtc0tuU1lyR05ZVDlRQ0xtNHlFSkxEUDRGbWh4RjFXOXpLZXRfNzB5VHBrM2dDcFBuMGpYdTVIM3VFcEJlcUxFU2dPU01SS1U5ZUdFWW1FRHBodVE4bmRnZ2lFLWxBd1J0WG0yMkVnaGl5bnFBN2JuMkd4Yw&q=https%3A%2F%2Fgithub.com%2Fctrlpvim%2Fctrlp.vim&v=hdZMqMeruSQ) [https://github.com/preservim/nerdcomm...](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbkF5cGYwZ0Q4NjFJUW5Lb2xPcUQyUVB6Z2tUUXxBQ3Jtc0tsdmY3R3ZOQzJhV29XNkJUSzdGdFZwdHV0Smw1LWJjVGdJVWpLRFlmS3ctWGxXbzNOc2p5X3lrQWd5cmhJQndBaHVNaUw1M29KblBtQ1o4V3loei1reGxydXp1LVhoQXVrcHk3UklIbUZzczNxaHQwdw&q=https%3A%2F%2Fgithub.com%2Fpreservim%2Fnerdcommenter&v=hdZMqMeruSQ) [https://github.com/mattn/emmet-vim](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbE1sc0lQQjhMekRnRVFJYmd2dnkzMFdzWEpUd3xBQ3Jtc0tuUGNWUjd2ZV9GakNNQlo4enYzNkhkXzlFM011RXVQdG9wTXBxdkI0cFRsUGtTbk1KM21LeXM4UG4wMHpiam1VU3N2OUh3TTJLTDJLaXBvazBRcGpGMGV3NW9rYl9Ealg3RHhBNXFmTWpSZF9GUk55RQ&q=https%3A%2F%2Fgithub.com%2Fmattn%2Femmet-vim&v=hdZMqMeruSQ) [https://github.com/dense-analysis/ale](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbGRoc3ZLUkluNmxPVmVsZ0VQRHVubTdQRDJrQXxBQ3Jtc0ttRVlIOEVjVktfUWFhNXg2S3hEQlA2ZFY3NThnWGlYTWRZeGM4UGNLWmFoeGRJRjN2ME9ObmxOX2h6QWI4dDhZdUpUelhvM0xhUTJKdVlFYjUxQ0N2aENQakZjbGFwUUQzWk5SbHVCRTJ1WEJ5V1Z0aw&q=https%3A%2F%2Fgithub.com%2Fdense-analysis%2Fale&v=hdZMqMeruSQ) [https://github.com/sheerun/vim-polyglot](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbnNzS1dfS2lrb2w3eld3ZUVVQzdNS0J1WEl2QXxBQ3Jtc0tsakptclNzaldLNmdoOW5RRVVDTlN3MDFCZGZSR2VsdzF3bXFSckZSRVRhQTNoNXc3dnVHUERuRVlXc0VETUxiczgxbjdWT1dIMG1tdHV6WVNoR1o0QjBOYTFYem51OWtaRUR6aUFfRjhZaDJzYWUzNA&q=https%3A%2F%2Fgithub.com%2Fsheerun%2Fvim-polyglot&v=hdZMqMeruSQ) [https://github.com/neoclide/coc.nvim](https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbk9NVGpSOENFX2NvbVhvc2NXMVM4dHRPYmxFZ3xBQ3Jtc0tsOG40a0YtbF9rZVpZWUlBTjVMdkppanhtU0JTUGNMenBoTTV1bkdwSlBLdmYwTDhNdFphTVVTd2g3SFdyN2RxVVJfbTBKbXRvYWkzRjlucFkwaWRRUHd0Njd6T1pNZ3NqX1d5U1Fwc3R1c0IwX2lUOA&q=https%3A%2F%2Fgithub.com%2Fneoclide%2Fcoc.nvim&v=hdZMqMeruSQ)






```python
```python
import keyboard

keyboard.write('Familia DIB.')
keyboard.send('ls+-R')







```