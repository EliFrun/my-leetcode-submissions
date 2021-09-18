/**
 * @param {number[][]} image
 * @param {number} sr
 * @param {number} sc
 * @param {number} newColor
 * @return {number[][]}
 */
var floodFill = function(image, sr, sc, newColor) {
    let curr = [[sr, sc]];
    let nextLayer = [];
    let visited = new Set();
    let val = image[sr][sc];
    
    while (curr.length > 0) {
        curr.forEach((a) => {
            let r = a[0];
            let c = a[1];
            image[r][c] = newColor;
            visited.add(`${r}_${c}`);
            if (r - 1 >= 0 && image[r - 1][c] == val && !visited.has(`${r - 1}_${c}`)) {
                nextLayer.push([r - 1, c]);
            }
            if (c - 1 >= 0 && image[r][c - 1] == val && !visited.has(`${r}_${c - 1}`)) {
                nextLayer.push([r, c - 1]);
            }
            if (r + 1 < image.length && image[r + 1][c] == val && !visited.has(`${r + 1}_${c}`)) {
                nextLayer.push([r + 1, c]);
            }
            if (c + 1 < image[0].length && image[r][c + 1] == val && !visited.has(`${r}_${c + 1}`)) {
                nextLayer.push([r, c + 1]);
            }
        });
        
        curr = nextLayer;
        nextLayer = [];       
    }
    
    return image;
};
