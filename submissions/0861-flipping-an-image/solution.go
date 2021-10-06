func flipAndInvertImage(image [][]int) [][]int {
    for _, v := range(image) {
        invertRow(v)
    }
    return image
}

func invertRow(row []int) {
    for i, j := 0, len(row) - 1; i <= j; i, j = i + 1, j - 1 {
        row[i], row[j] = 1 - row[j], 1 - row[i]
    }
}
