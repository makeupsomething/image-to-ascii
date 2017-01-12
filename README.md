# image-to-ascii
A small python tool that converts images to ascii art

##Dependencies

Pillow - for image processing

https://python-pillow.org/

Begins - makes creating command line applications in Python easy

http://begins.readthedocs.io/en/latest/index.html

## Usage

For a simple image conversion run the following

`python converter_cli.py --image-file-path sample_images/isaax.jpg`


To see the list of arguments run

`python converter_cli.py -h`

## Future work

- More character options, multiple different ASCII characters representing different shades
- Save to file option
- A GUI version


## Some images generated with this tool

```
                                                                                                                        
   *                 *           *              *            *         *   *******        *                *            
    *              **           *               *            *         *                  *                *            
     *            **           *                *            *         *                  *                *            
      *          **           *                 *            *         *                  *                *            
      **        **           *                  *            *         *                  *                *            
        *      **          **                   *            *         *                  *                *            
         *    **          **                    *            *         *                  *                *            
          *  *           **                     *            *         *                  *                *            
                              *******           *  ********  *         *   *******        *                *            
          *  *                          *       *            *         *                  *                *            
         *    **                       *        *            *         *                  *                *            
        *      **                     *         *            *         *                  *                *            
      **        **                  **          *            *         *                  *                *            
      *          **                **           *            *         *                  *                *            
     *            **              **            *            *         *                  *                *            
    *              **            **             *            *         *                  *                *            
   *                 *          **              *            *         *   *******        *  *******       *   *******  
                                                                                                                        
```

```
                                          .....
                                      .........   .
                                    ..........   ....
                                   ..........    .....
                                   ..........   ......
                                  ..........   ............
                              .   .........   ..............
                          ....    ........    ..............   .........
                         .....   .......     ............     .........
                        .....   .....         ........         .......    ..
                       .....   .....   .....   ......   .....   ......   ....
                       ....    ....    .....   ......   .....    ....   .....
                       ....   ......    ...    ......     ..    ....   ......
                        ..   .........       ..........       .....    .....
                             ........    ..............   .........   .....
                            .........   ..............   .........   ....
                                ....   ..............    ........


                        ..

                        ..     ........  ........     ........    ...     ..
                        ..   ...                ...         ....   ..     ..
                        ..    ....           ... ...     .... ..    .  ...
                        ..       .....    ...... ...  ....... ..    ....  .
                        ..          ...  ...    ...   ..     ...   ..    ...
                        ..   ........    ........     ........    ...     ..
```
